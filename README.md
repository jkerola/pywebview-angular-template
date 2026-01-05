# PyWebView + Angular Template

Application template for creating native python applications with Angular as the frontend framework. Uses pywebview to render the application using the system native webview.

## Dependencies

Angular dependencies are managed with NPM. Python dependencies with pip.

**Requirements**:

- Python 3.9+
- Nodejs v22+

```shell
# Install NPM dependencies
npm install

# Recommended: Install dependencies in a virtual environment
python3 -m venv env
source env/bin/activate

# Python dependencies for Windows, Mac
pip install pywebview watchdog

# Linux specific choice between GTK and QT
# pywebview[gtk] preferred, as pywebview[qt] tends to crash
pip install pywebview[gtk] watchdog
```

## Development

The application uses `watchdog` to reload frontend changes when started with the `--reload` flag. The `--debug` flag enables the developer console. For production builds, it is recommended to disable these features.

```shell
# Start the angular build in watch mode
ng build --watch

# In a separate terminal, start the application
python3 app.py --reload --debug
```

## Building

Build output is stored in `dist`. Be sure to build the frontend before building the application bundle. Use `ng build` to ensure the latest changes are reflected in the application.

To build all possible outputs, use `npm run build`.

### PyInstaller

A pre-configured build specification for a single-file executable is provided with the `build.spec` file.

```shell
pyinstaller build.spec
```

### Wheel

A pre-configured build specification for a python wheel is provided in the `pyproject.toml` file.

```shell
python -m build
```

## API typing

The `src/app/window.interface.ts` contains the typescript definitions for the `src/python/api.py` class. It is recommended to update the types when modifying the API. Note that all functions return a `Promise<type>`, which can be converted into an observable using the `from` function from `rxjs`.
