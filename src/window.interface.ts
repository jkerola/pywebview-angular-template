// Import your types used with the API here.

declare global {
  interface Window {
    pywebview: {
      /**
       * Include your API typing here.
       *
       * Please see 'src/python/api.py' for the python code.
       *
       * Note that return types are all Promises, not Observables.
       */
      api: {
        greet: (name: string) => Promise<string>;
      };
    };
  }
}

export {};
