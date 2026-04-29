# AGENTS.md — Architekt

## Project Overview

**Architekt** is a PySide6/Qt desktop GUI application for managing variables and devices in embedded system architecture configurations. It provides a tabbed interface where users define variables with typed properties and assign source/destination devices to each variable.

## Running the Application

```bash
pip install -r requirements.txt
python architekt.py
```

No build step required. Python 3.x required (tested on 3.13).

## Repository Layout

```
architekt.py              # Entry point — creates QApplication, loads config, shows MainWindow
config.ini                # Configurable data types and device names
requirements.txt          # PySide6, configparser, icon
src/
  mainwindow.py           # Main window: tab setup, delegate wiring, add/remove row buttons
models/
  column.py               # Column enum (all column name constants)
  tablemodel.py           # Base QAbstractTableModel backed by a pandas DataFrame
  variabletablemodel.py   # TableModel subclass for Variables tab (7 columns)
  devicetablemodel.py     # TableModel subclass for Devices tab (1 column: Name)
delegates/
  combobox.py             # QItemDelegate — single-value dropdown from config.ini
  multiselect.py          # QItemDelegate — multi-value checkbox list (comma-separated output)
ui/
  form.ui                 # Qt Designer XML source
  ui_form.py              # Auto-generated Python class from form.ui (do not edit manually)
img/
  icon.png                # Application icon
```

## Architecture

The project follows a straightforward MVC pattern:

- **Model layer** (`models/`): `TableModel` wraps a pandas DataFrame and implements the Qt model interface. Subclasses (`VariableTableModel`, `DeviceTableModel`) declare their columns. Callbacks `onChange` and `onRemove` notify the controller of data changes.
- **Controller/View** (`src/mainwindow.py`): `MainWindow` instantiates both models, sets up `QTableView` delegates column-by-column, and wires add/remove row buttons. It also handles syncing device renames into the Variables table.
- **Delegates** (`delegates/`): `ComboboxDelegate` renders a `QComboBox` for single-value columns (Type, Publishing mode, Source Device). `MultiSelectDelegate` renders a `QListWidget` with multi-selection for the Destination Devices column.

**Data flow:**

```
config.ini ──► MainWindow ──► VariableTableModel (pandas DataFrame)
                         └──► DeviceTableModel   (pandas DataFrame)
                                    │
                         QTableView + Delegates (per-column cell editors)
```

## Configuration

`config.ini` controls runtime-configurable options:

```ini
[types]
value = uint8 uint16 uint32 int8 int16 int32 float32   # Variable data types

[devices]
dev = wheel vcu cooling pc                              # Available device names
```

Adding a new type or device: edit the appropriate space-separated list in `config.ini` — no code changes needed.

Adding a new column: update the `Column` enum in `models/column.py`, add the column to the relevant model subclass, and wire a delegate in `mainwindow.py`.

## Key Implementation Details

- All table data is stored in pandas DataFrames (`_data` attribute on `TableModel`). Row insertion appends a new row of empty strings; row deletion uses `DataFrame.drop`.
- Destination Devices are stored as a comma-separated string in a single cell (e.g., `"wheel,vcu"`). `MultiSelectDelegate` splits/joins on comma.
- Device renames propagate to Variables: `MainWindow` passes an `onChange` callback to `DeviceTableModel` that rewrites affected cells in the Variables table.
- `ui_form.py` is auto-generated from `form.ui` by Qt's `uic` tool — do not edit it directly. Regenerate with: `pyside6-uic ui/form.ui -o ui/ui_form.py`

## Known Gaps / TODOs

- **Export is a stub** (`mainwindow.py:84–90`): prints device names to stdout, no actual file output.
- **Menu actions unconnected**: File → Open/Save/Close and Help → About are defined in the UI but have no signal handlers.
- **No data persistence**: table contents are lost on close.
- **MultiSelectDelegate** does not pre-select already-stored values when the editor opens.
- **No tests**: no test directory or framework configured. Models and delegates are good candidates for pytest unit tests.
- One `# TODO` in `mainwindow.py:79` — device-deletion cleanup logic should move into the model's `onRemove` callback.

## Development Notes

- Type hints are present in some places, absent in others — favour adding them in new code.
- No docstrings anywhere; keep new docstrings to one short line if added.
- Error handling is minimal by design at this prototype stage; a `try/except` exists only in `TableModel.removeRow`.
- There is no CI, linter config, or formatter config. Use standard Python style (PEP 8).
