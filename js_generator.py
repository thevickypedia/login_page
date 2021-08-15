from os import environ, path, system
from webbrowser import open as web_open


def raw_js() -> str:
    """Raw JavaScript for login page - client side authentication.

    Returns:
        str:
        JavaScript with placeholder values for ``Username`` and ``Password``.
    """
    return """const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "USERNAME_HERE" && password === "PASSWORD_HERE") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})"""


def login() -> tuple:
    """Takes ``Username`` and ``Password`` from environment variables.

    Prompts for ``Username`` and ``Password`` if not found in ``env vars``.

    Returns:
        tuple:
        A tuple of the ``username`` and ``password``.
    """
    if not (username := environ.get('USERNAME')):
        username = input('Enter an username for your login page:\n')
    if not (password := environ.get('PASSWORD')):
        password = input('Enter a password for your login page:\n')
    return username, password


def obfuscate(temp_file: str, js_file: str = 'login-page.js') -> str:
    """Command to obfuscate the ``JavaScript`` and write it as a file.

    Args:
        temp_file: Temporary file name which will be removed once the obfuscator command completes.
        js_file: JavaScript file that is named in the ``index.html``

    Returns:
        str:
        ``JavaScript`` obfuscator command.
    """
    # noinspection LongLine
    return f"javascript-obfuscator {temp_file} --options-preset high-obfuscation --target browser --seed 0 --self-defending true --debug-protection true --debug-protection-interval true --string-array true --rotate-string-array true --shuffle-string-array true --string-array-threshold 1 --string-array-index-shift true --string-array-indexes-type hexadecimal-numeric-string --string-array-wrappers-count 5 --string-array-wrappers-type function --string-array-wrappers-parameters-max-count 5 --string-array-encoding rc4 --split-strings true --identifier-names-generator hexadecimal --compact true --simplify true --transform-object-keys true --numbers-to-expressions true --control-flow-flattening true --control-flow-flattening-threshold 1 --dead-code-injection true --dead-code-injection-threshold 1 --output {js_file}"  # noqa: E501


def trigger() -> None:
    """Controller for rest of the functions.

    Triggers:
        - ``login()`` function to get the ``Username`` and ``Password``
        - ``raw_js()`` function to get the ``JavaScript`` with replaced placeholder values.
        - ``obfuscate()`` function to get the command to obfuscate.

    Removes the temp file once the work is done.
    """
    user_, pass_ = login()
    write = raw_js().replace('USERNAME_HERE', user_).replace('PASSWORD_HERE', pass_)
    temp_f = 'placeholder.js'
    with open(temp_f, 'w') as file:
        file.write(write)
    system(f'{obfuscate(temp_file=temp_f)} && rm {temp_f}')
    web_open('file://' + path.realpath('index.html'))


if __name__ == '__main__':
    trigger()
