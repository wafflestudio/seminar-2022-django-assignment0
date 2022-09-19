<!-- TODO -->
# CatFact API Docs

Summary : 품종별 catfact를 등록하고 / 수정하고 / 삭제하는 Rest API


## API Description

| method | url                                 | Description                           | Response                                     |
|--------|-------------------------------------|---------------------------------------|----------------------------------------------|
| POST   | catfact/user/                       | create user                           | `HTTP201`, `HTTP400`                         |
| POST   | catfact/login/                      | login                                 | `HTTP200`, `HTTP400`                         |
| GET    | catfact                             | return a list of all breeds of cat    | `HTTP200`, `HTTP400`                         |
| GET    | catfact/\<int:pk\>                  | return breed whose pk is correct      | `HTTP200`, `HTTP400`, `HTTP404`              |
| POST   | catfact/                            | add new breeds info                   | `HTTP200`, `HTTP400`, `HTTP401`, `HTTP403`   |
| PUT    | catfact/\<int:pk\>                  | modify breed whose pk is correct      | `HTTP200`, `HTTP400`, `HTTP401`              |
| DELETE | catfact/\<int:pk\>                  | delete breed whose pk is correct      | `HTTP200`, `HTTP400`, `HTTP401`              |

### I. Create User

```bash
curl --request POST \
     --url http://catfact/user/ \
     --header 'email: user1@example.com' \
     --header 'username: user1' \
     --header 'password: password1' 
```

### II. Login

```bash
curl --request POST \
     --url http://catfact/login/ \
     --header 'username: user1' \
     --header 'password: password1'
```

### III. Get Cat Breed info (Only for Authorized Users)

```bash
curl --request POST --url http://catfact/ 
curl --request POST --url http://catfact/\<int:pk\> 
```

### IV. Add New Breed info (Only for Authorized Users)


```bash
curl --request POST \
     --url http://catfact/ \
     --header 'name: breed_name' \
     --header 'description: script' \
```

### V. Edit Info (Only for Authorized Users)

```bash
curl --request PUT --url http://catfact/\<int:pk\> 
curl --request DELETE --url http://catfact/\<int:pk\> 
```