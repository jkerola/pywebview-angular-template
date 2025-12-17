interface Window {
  pywebview: {
    /**
     * Include your API typing here.
     *
     * Please see 'src/python/api.py' for the python code.
     */
    api: {
      greet: (name: string) => Promise<string>;
    };
  };
}
