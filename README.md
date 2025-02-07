# ssrf-app
Server-side request forgery Vulnerability implement application.

### API healthcheck ❤️
```sh
/v1/health
```
return : 

```sh
{"status": "200 OK"}
```

### API / main page 
```sh
/
```

return :

<img src="./API/main.jpg" alt="main.com" width="104" height="142">

### API SSRF Attack
```sh
/v1/image?url=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLZf31OpU0zqzpDS-IwNBp7lF1eejh9YJHHA&s
```

return :

<img src="./API/ssrf.jpg" alt="ssrf.com" width="104" height="142">