from configparser import ConfigParser

config = ConfigParser()

config["JFROG"] = {
    "hostJFrog": "http://192.168.10.200:8088/artifactory/",
    "usernameJFrog": "sanja",
    "passwordJFrog": "eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiJkdjJ0V3pWX3podldndGs3X2ktZlZ6R3BJSnFGdFZ3dGQzWlpuMThwNE13In0.eyJleHQiOiJ7XCJyZXZvY2FibGVcIjpcInRydWVcIn0iLCJzdWIiOiJqZmFjQDAxZ216Nm5lanhoZ2N5MHd0ZTEwYWgxd2h6XC91c2Vyc1wvc2FuamEiLCJzY3AiOiJhcHBsaWVkLXBlcm1pc3Npb25zXC9hZG1pbiIsImF1ZCI6IipAKiIsImlzcyI6ImpmZmVAMDAwIiwiaWF0IjoxNjczMjY4ODQ5LCJqdGkiOiI5ODIzNmRiNC0zM2NiLTQwNzctYjdhZi04NjI0NTI2MDBmODIifQ.lTqUunLEsq3y0Gzwo-YNvOzQvixWmhtamDQu_5Bw_xm6IJNwUN_rv9pJa8mdM5C18RETpbY4d2JQHl0nPnscuz9mvUPxJkNvSZibCMz_9hqErb2Un-B1bqhkXvt8fnVclJgfbuPhycaPc4pdVhLIzC7MBLEP6Fy7OwtaTUxyTg0Jz47R5I35jYk7znW7r4oud1EtMwo7sNytW-a4HciW1CaxCJWvyLuj_kasZ7rfCw45AnXvbW0wqbRiR9QfXk5zDU_dwQO4VMLhqeYTtcU9s8U8k4M1zSn6vvrHrBTKURqEg9zJ_i-Q5nKodC0g2Jyx79besVU9DtF_VAu1KVdtOw",
    "url_projects": "http://192.168.10.200:8082/api/v4/users/svukelic/projects",
}

with open("parametersjfrog.ini", "w") as f:
    config.write(f)
