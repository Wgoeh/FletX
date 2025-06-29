## 🇫🇷 FletX CLI - Documentation

### Introduction

Le **CLI de FletX** (`fletx`) est un outil en ligne de commande qui facilite la gestion des projets **FletX**. Il vous permet de :

* Créer un nouveau projet FletX
* Générer des composants (contrôleurs, services, pages, etc.)
* Exécuter votre projet avec différentes options

---

### Commande principale

```bash
fletx <commande> [options]
```

---

### Commandes disponibles

| Catégorie              | Commande   | Description                                              |
| ---------------------- | ---------- | -------------------------------------------------------- |
| **Gestion de projet**  | `new`      | Crée un nouveau projet FletX à partir d'un modèle        |
| **Génération de code** | `generate` | Génère des composants comme des contrôleurs, services... |
| **Utilitaires**        | `run`      | Exécute un projet FletX avec diverses options            |

👉 **Aide spécifique :**

```bash
fletx <commande> --help
fletx help <commande>
```

---

### `fletx new`

Créer un nouveau projet FletX.

```bash
fletx new <nom_du_projet> [options]
```

#### Options

| Option                            | Description                                     | Par défaut      |
| --------------------------------- | ----------------------------------------------- | --------------- |
| `--template TEMPLATE`             | Modèle à utiliser pour le projet                | `project`       |
| `--directory DIRECTORY`           | Dossier où créer le projet                      | dossier courant |
| `--author AUTHOR`                 | Nom de l'auteur                                 |                 |
| `--description DESCRIPTION`       | Description du projet                           |                 |
| `--version VERSION`               | Version initiale du projet                      | `0.1.0`         |
| `--python-version PYTHON_VERSION` | Version minimale de Python requise              | `3.12`          |
| `--overwrite`                     | Écrase les fichiers existants si présents       |                 |
| `--no-install`                    | Ne pas installer les dépendances après création |                 |

---

### `fletx generate`

Générer un composant de votre projet.

```bash
fletx generate <type> <nom> [options]
```

où `<type>` peut être : `controller`, `service`, `model`, `component`, `page`

#### Options

| Option                    | Description                                 | Par défaut       |
| ------------------------- | ------------------------------------------- | ---------------- |
| `--output-dir OUTPUT_DIR` | Dossier de sortie                           | basé sur le type |
| `--template TEMPLATE`     | Modèle spécifique à utiliser                | basé sur le type |
| `--overwrite`             | Écrase les fichiers existants               |                  |
| `--with-test`             | Génère un fichier de test pour le composant |                  |

---

### `fletx run`

Exécutez votre projet FletX.

```bash
fletx run [target] [options]
```

où `target` est le fichier Python à exécuter (par défaut : `main.py`)

#### Options

| Option                        | Description                                      | Par défaut  |
| ----------------------------- | ------------------------------------------------ | ----------- |
| `--host HOST`                 | Hôte de liaison                                  | `localhost` |
| `--port PORT`                 | Port de liaison                                  | `8550`      |
| `--debug`                     | Mode debug                                       |             |
| `--watch`                     | Active le hot reload (surveillance des fichiers) |             |
| `--web`                       | Ouvre dans un navigateur web                     |             |
| `--desktop`                   | Force le mode desktop                            |             |
| `--android`                   | Ouvre sur un appareil Android                    |             |
| `--ios`                       | Ouvre sur un appareil iOS                        |             |
| `--assets-dir ASSETS_DIR`     | Dossier des assets                               |             |
| `--ignore-dir IGNORE_DIR`     | Dossier à ignorer                                |             |
| `--env ENV`                   | Variables d'environnement `KEY=VALUE`            |             |
| `--requirements REQUIREMENTS` | Fichier `requirements.txt` à utiliser            |             |
| `--install-deps`              | Installe les dépendances avant d'exécuter        |             |
| `--verbose`                   | Affiche des logs détaillés                       |             |

---

### Exemple : Création et exécution

```bash
# Créer un projet
fletx new mon_projet --author "Jean Dupont" --description "Mon app FletX"

# Générer un contrôleur
fletx generate controller MonControleur --with-test

# Exécuter le projet
fletx run --web --debug
```

---

## 🇬🇧 FletX CLI - Documentation

### Introduction

The **FletX CLI** (`fletx`) is a command-line tool that makes it easy to manage **FletX** projects. It lets you:

* Create a new FletX project
* Generate components (controllers, services, pages, etc.)
* Run your project with various options

---

### Main command

```bash
fletx <command> [options]
```

---

### Available commands

| Category               | Command    | Description                                          |
| ---------------------- | ---------- | ---------------------------------------------------- |
| **Project Management** | `new`      | Create a new FletX project from template             |
| **Code Generation**    | `generate` | Generate components like controllers, services, etc. |
| **Utilities**          | `run`      | Run a FletX project with various options             |

👉 **Specific help :**

```bash
fletx <command> --help
fletx help <command>
```

---

### `fletx new`

Create a new FletX project.

```bash
fletx new <project_name> [options]
```

#### Options

| Option                            | Description                                           | Default           |
| --------------------------------- | ----------------------------------------------------- | ----------------- |
| `--template TEMPLATE`             | Template to use for the project                       | `project`         |
| `--directory DIRECTORY`           | Directory where the project will be created           | current directory |
| `--author AUTHOR`                 | Author name for the project                           |                   |
| `--description DESCRIPTION`       | Project description                                   |                   |
| `--version VERSION`               | Initial version of the project                        | `0.1.0`           |
| `--python-version PYTHON_VERSION` | Minimum required Python version                       | `3.12`            |
| `--overwrite`                     | Overwrite existing files if they exist                |                   |
| `--no-install`                    | Don't install dependencies after creating the project |                   |

---

### `fletx generate`

Generate a component for your project.

```bash
fletx generate <type> <name> [options]
```

where `<type>` can be: `controller`, `service`, `model`, `component`, `page`

#### Options

| Option                    | Description                            | Default       |
| ------------------------- | -------------------------------------- | ------------- |
| `--output-dir OUTPUT_DIR` | Output directory                       | based on type |
| `--template TEMPLATE`     | Specific template to use               | based on type |
| `--overwrite`             | Overwrite existing files               |               |
| `--with-test`             | Generate a test file for the component |               |

---

### `fletx run`

Run your FletX project.

```bash
fletx run [target] [options]
```

where `target` is the Python file to run (default: `main.py`)

#### Options

| Option                        | Description                         | Default     |
| ----------------------------- | ----------------------------------- | ----------- |
| `--host HOST`                 | Host to bind to                     | `localhost` |
| `--port PORT`                 | Port to bind to                     | `8550`      |
| `--debug`                     | Run in debug mode                   |             |
| `--watch`                     | Enable hot reload (directory watch) |             |
| `--web`                       | Open in a web browser               |             |
| `--desktop`                   | Force desktop mode                  |             |
| `--android`                   | Open on an Android device           |             |
| `--ios`                       | Open on an iOS device               |             |
| `--assets-dir ASSETS_DIR`     | Path to assets directory            |             |
| `--ignore-dir IGNORE_DIR`     | Path to ignore directory            |             |
| `--env ENV`                   | Environment variables `KEY=VALUE`   |             |
| `--requirements REQUIREMENTS` | Path to `requirements.txt` file     |             |
| `--install-deps`              | Install dependencies before running |             |
| `--verbose`                   | Verbose output                      |             |

---

### Example: Create and run

```bash
# Create a project
fletx new my_project --author "John Doe" --description "My FletX app"

# Generate a controller
fletx generate controller MyController --with-test

# Run the project
fletx run --web --debug
```
