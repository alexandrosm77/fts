# Django Development Test (suggested 3 hours max.)

## Instructions
* Get the project running using Docker (full instructions below) and familiarise yourself with its operation.
* Complete the following development tasks.  The first three can be completed in any order and it's OK if you don't get them all done in time, just push what you have after 3 hours:
    1. Users have requested a way to create groups of `Instruction` instances.  Please create a new `InstructionGroup` model that can be used to relate `Instruction` instances to each other. When an `Instruction` is in an `InstructionGroup`, render a link against that `Instruction` record on the homepage (http://127.0.0.1:8000/forensic/instructions/) that will open a new page that lists all of the `Instruction`s in that `InstructionGroup`.
    2. Users have reported that the homepage (http://127.0.0.1:8000/forensic/instructions/) and the "Problematic Instructions" page (http://127.0.0.1:8000/forensic/instructions/with-too-many-hair-samples/) are both very slow to load.  Please see if you can improve their performance.
    3. Refactor the existing `too_many_hair_samples()` FBV into a suitable CBV for consistency with the other views.
    4. Optional stretch goal once the above have been completed: make any other changes or improvements that you see fit. For example improving the UI, adding pagination, unit tests or documentation. 
* Push your work to a git repository (Github or Gitlab preferred).  If the repository is private you must invite the following accounts as contributors so we can see review your work at the time you submit it - Github: "ftstim" & "asday", Gitlab: "t.jones" & "Asday".
* Email a link to your repository to it@forensic-testing.co.uk

If you have any problems during this test we are happy to help, please get in contact with us ASAP at it@forensic-testing.co.uk or by phoning 07939205076 (between 6am and midnight).

## Requirements to run the project

* Linux
* Docker 20.10 or higher ([CentOS](https://docs.docker.com/install/linux/docker-ce/centos/), [Debian](https://docs.docker.com/install/linux/docker-ce/debian/), [Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/), [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/), [Arch](https://wiki.archlinux.org/title/Docker#Installation));
* `docker-compose`, version 2.0.0 or higher (Linux only, instructions [here](https://docs.docker.com/compose/install/));
* [bash](https://www.gnu.org/software/bash/) to use the convenience scripts in [`bin/`](bin/);
* either have `EDITOR` set, or have [nano](https://www.nano-editor.org/download.php) installed;
* [direnv](https://direnv.net/) to benefit from automatic `.envrc` management - it's possible to get by without this, but in that case, `source .envrc` is required in every new shell, and cleaning up the environment upon leaving the project is the responsibility of the reader.

## How to run the project

Run `./bin/install` to run the automated setup.  This will build the docker containers, ask you to configure custom ports and docker/docker-compose command lines (if you require it) and set up the database.  Once everything is ready, the project will be started in the background, and you will be left with a usable terminal.

By default, you will then be able to access the project at [http://127.0.0.1:8000](http://127.0.0.1:8000).  Other services are by default exposed on ports 5555 (Celery's Flower), 8025 (mailpit's web interface), and 1313 (Hugo's static site), and may or may not be useful to you during your development.

> From this point on, it will be assumed that your `PATH` contains `$PWD/bin`.  This will automatically be the case if you have `direnv` installed.  If this is not the case, commands must be run in the form `./bin/command-name` rather than `command-name`.

To stop the project, run `stop`.  To start it again, run `start`.  If you'd like to view the console of the running project, run `logs`.

As the project is dockerised, management commands must be run within the container.  The command `manage` is available for this purpose, and can be invoked in the same way as non-dockerised Django projects, for example:

* non-dockerised `(env) $ python manage.py migrate`;
* dockerised `$ manage migrate`.

For more commands, see [`bin/`](bin/).

## Uninstallation

Should anything go wrong during installation, or should you no longer wish to work on the project, run `uninstall` to clean up.  Your `.envrc` will be left in place to save your configuration for convenience, and must be manually `rm .envrc`'d if you would like a completely clean start.

## Files

Path | Description
-|-
[`bin/`](bin/) | Convenience scripts for development.
[`docker/`](docker/) | Implementation-detail persistent storage and build files for the docker containers.
[`docs/`](docs/) | Documentation oriented towards developers.
[`manual/`](manual/) | Documentation oriented towards users.
[`requirements/`](requirements/) | Source of truth for python requirements files, divided by independent subsection.
[`src/`](src/) | Source code.
[`tests/`](tests/) | Test source code only.
`.editorconfig` | Description of code style.
`.envrc` | Developer-specific project configuration.
`.flake8` | Linting configuration file.
`.gitignore` | Project-wide source control ignores to deal with developer-specific state and cached Python bytecode.
`.installed` <br /> `.built` <br /> `.completions-generated` <br /> `.migrated` | Semaphores for the [installation](bin/install) and [uninstallation](bin/uninstall) scripts.
`.isort.cfg` | Linting configuration file specifically dealing with import sorting.
`docker-compose.yml` | Project specification.
`example.envrc` | Template project configuration.
