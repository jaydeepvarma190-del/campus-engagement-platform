from database import cursor, conn


def register(
    name,
    email,
    password
):

    cursor.execute(
        """
        INSERT INTO users
        (
        name,
        email,
        password
        )

        VALUES
        (
        ?,
        ?,
        ?
        )
        """,

        (
            name,
            email,
            password
        )
    )

    conn.commit()


def login(
    email,
    password
):

    cursor.execute(
        """
        SELECT *
        FROM users

        WHERE email=?
        AND password=?
        """,

        (
            email,
            password
        )
    )

    user = cursor.fetchone()

    return user