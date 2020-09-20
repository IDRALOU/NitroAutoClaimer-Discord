# Punchnox Project Api

__Je vous recommande d'utiliser postman pour effectuer les requêtes.__


**Sinon vous pouvez faire vôtre propre code.**

<details markdown='1'><summary>Exemple</summary>

```js
const snekfetch = require("snekfetch");

snekfetch.post("https://punchnox-project-api.herokuapp.com/api/logs/connect").send({
"Username": "le username" 
}).end((err, res) => {
  if(err) { 
  console.log(err) 
  } else {
  console.log(res.body)
  }
})
```

</details>

**Toutes les requêtes utilisent la méthode ``"POST"`` sauf sur la page d'accueil et l'endpoint :**

*.../api/update/infos*

  *[lien](https://punchnox-project-api.herokuapp.com/api/update/infos)*

```js
const snekfetch = require("snekfetch");

snekfetch.get("https://punchnox-project-api.herokuapp.com/api/update/infos")
.then((err, res) => {
  if(err) { 
  console.log(err) 
  } else {
  console.log(res.body)
  }
});
```


***Je mettrais à disposition un lien pour avoir accès au ``workspace`` pour effectuer les requêtes sur postman.***


Les administrateurs aurons un mot de passe pour effectuer les requêtes.

>  ⚠️ **Attention** Si je vois que des actions _(ajouts de membres en premium sans raison valable, blackliste ou même actions effectuées par d'autres membres que ceux du staff)_ je le verais donc la suppression du mot de passe et ajout dans la blackliste sera effectué.





# Enregistrer un client premium.

J'ai fais un tools qui permet de générer une clée random assez complexe pour que se ne sois pas brut force.



 *Alors pour ça je vais faire un exemple avec postman:*
 
 1. Vous créez une requête 
 2. Vous mettez l'url `l'endpoint` et vous mettez la requête en `POST`
 3. Une fois fait vous allez sur body, vous le mettez en format `json` et pour finir vous mettez ça 
 
 ```json
 {
   "Key": "la key (key que vous auriez généré auparavant)",
   "Username": "le username du client",
   "User_id": "l'id du client",
   "Raison": "la raison pour laquelle le client est premium (payment/boost/invites)",
   "Password": "votre mot de passe"
}
 ```
 
 4. Pour finir vous faites `send`
 Et voila un message va apparaître comme quoi l'utilisateur a bien été enregistré.
 
 
 
#  Blacklist 

**Pour mettre un utilisateur en blackliste vous aurez besoin de son adresse ip.
Pour se faire il faut que le client ai déjà utilisé le selfbot ou vous récupérez son ip à votre façon.**

**Pour récupérer l'adresse ip du client vous devrez vous retrouver sur la base de donnée du selfbot (`seule les administrateurs du selfbot peuvent y avoir accès`).
Je vous conseille de télécharger mongo compass.
Une fois installé vous aurez un url dans le quel vous mettrez vos identifiants pour vous connecter (`les identifiants changerons toutes les semaines question dr sécurité`).**


Mettre un screen 

**Vous aurez donc accès à une partie du cluster Vous vous rendrez sur le model `connexion`**

 (Mettre un screen)
 
**Puis cliquez sur la recherche rentrez son id**

Mettre un screen


**Si le client a déjà utilisé le selfbot vous aurez son adresse ip comme indiqué sur le screen**

Mettre un screen 


**Il vous suffit alors d'allez sur postman faire une requête comme dit précédemment ou rejoindre le `workspace`, aller dans le body `json` et mettre ceci :**


```json
{
"Ip": "l'adresse ip du client",
"Username": "Username du client le jour de la blackliste",
"Id": "l'id discord du client",
"Reason": "la raison pour laquelle le client est en blacklist",
"Password": "vôtre mot de passe"
}
```

**Vous faites comme au paravent (`cliquer sur send`), et si tous se passe comme prévu un message va apparaître en disant que le client a bien été blacklist.**









## les Endpoints

### Authentification :

> Auth signup (pour site web) :
_```...api/auth/signup```_

> Auth signin (pour site web) :
 _``...api/auth/signin``_

### Logs

> Logs connexions :
 _``...api/logs/connect``_

> Logs raid :
 _``...api/logs/raidlogs``_

> Logs reports :
 _``...api/logs/report``_

> Logs demande blacklist :
 _``...api/logs/black``_

### Premium 

> `Register client premium :
    _``...api/premium/register``_

>  Login via key :
_``...api/premium/login``_


### Blackliste et infos update

> Check si un membre est blacklist :
_``...api/update/blackliste``_

> Enregistrer un membre dans la blacklist :
_``...api/update/blackliste-register```_


> Check si un serveur est dans la blacklist :
_``...api/update/serveur-blackliste``_

> Enregistrer un serveur dans la blacklist :
_``...api/update/serveur-register``_

> Informations du selfbot :
_``...api/update/infos``_

> Modifier les informations du selfbot :
_``seulement disponible pour punchnox``_


### users info

**Méthode : `GET`**
**Headers : access_key + json web token**

> Voir si des utilisateurs ont utiliser l'api pour s'enregistrer (pour site web) :
_``...api/test/all``_

> Permet de se connecter en tant que `user` :
_``...api/test/user``_

> Permet de se connecter en tant que `mod` :
_``...api/test/mod``_

> Permet de se connecter en tant que `admin` :
 _``...api/test/admin``_
