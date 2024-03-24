db.createUser(
    {
        user    : "admin",
        pwd     : "password",
        roles   : [
            {
                role : "root",
                db   : "my-mongo-db"
            }
        ]
    }
)