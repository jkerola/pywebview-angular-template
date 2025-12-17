class Api:
    """Application API

    Serialized into the 'window.pywebview.api' object on typescript side.
    Please see the typings in 'src/app/typings.d.ts'.
    """

    def greet(self, name: str) -> str:
        """Return a greeting based oon [name].

        Args:
            name (str): Name to greet

        Returns:
            str: Greeting based on [name]
        """
        return f"Hello {name}!"
