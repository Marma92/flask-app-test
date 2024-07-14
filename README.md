# Gestion des Utilisateurs avec Flask

Cette application web permet de gérer une liste d'utilisateurs en utilisant Flask. Vous pouvez ajouter, modifier et supprimer des utilisateurs via une interface utilisateur interactive. Les actions sont effectuées via une API RESTful, garantissant une mise à jour en temps réel sans avoir besoin de recharger la page.

## Fonctionnalités

- Ajouter un utilisateur
- Modifier un utilisateur
- Supprimer un utilisateur
- Afficher la liste des utilisateurs

## Prérequis

- Python 3.x
- pip

## Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/Marma92/peticrud.git
cd votre-projet
```

2. Installez les dépendances :

```bash
pip install flask flask-restful
```

3. Utilisation

Lancez l'application Flask :

```bash
python app.py
```

Puis ouvrez votre navigateur et accédez à <http://127.0.0.1:5000>.

4. Routes API

   GET /api/users : Récupère la liste des utilisateurs.
   POST /api/users : Ajoute un nouvel utilisateur.
   GET /api/user/<user_id> : Récupère les détails d'un utilisateur spécifique.
   PUT /api/user/<user_id> : Modifie un utilisateur existant.
   DELETE /api/user/<user_id> : Supprime un utilisateur.

## Licence

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.
