# Installation Notes: `pip.ini` File

## Config file

`pip` allows you to set all command line option defaults in a standard ini style config file. The names
and locations of the configuration files vary slightly across platforms. You may have per-user, per-virtualenv
or global (shared amongst all users) configuration:

### Per-user

On **Unix** the default configuration file is: `\$HOME/.config/pip/pip.conf` which respects the `XDG_CONFIG_HOME` environment variable.

On **macOS** the configuration file is `$HOME/Library/Application Support/pip/pip.conf` if directory `$HOME/Library/Application Support/pip exists else \$HOME/.config/pip/pip.conf`.

On **Windows** the configuration file is `%APPDATA%\pip\pip.ini`.

### Missing Windows Bug

If you were like me, and you went to `%APPDATA%\pip\pip.ini` file you found it didn't exist. In fact, the entire `pip` folder did not exist either.
This makes it hard to leverage custom configurations using `pip`. The work around is you need to manually create this file. Follow the steps
below to resolve the issue:

1. Go to the `%APPDATA%` folder.
2. Create a new folder called `pip` if it does not exist.
3. Inside the `pip` folder create a file called `pip.ini`.
4. Inside that file, let's test out a custom configuration by putting the following configuration in the file:

   ```console
   [list]
   format=json
   ```

5. Run the following command in the terminal:

   ```console
   pip list
   ```

You should see the following output:

```json
[
  { "name": "adal", "version": "1.2.4" },
  { "name": "astroid", "version": "2.4.2" },
  { "name": "autopep8", "version": "1.5.3" },
  { "name": "azure-common", "version": "1.1.25" },
  { "name": "azure-core", "version": "1.8.0" },
  { "name": "azure-identity", "version": "1.4.0" }
]
```

From this point forward you should be able to use the `%APPDATA%\pip\pip.ini` command. The full path on my system looks like the following:

```console
C:\Users\Alex\AppData\Roaming\pip\pip.ini
```
