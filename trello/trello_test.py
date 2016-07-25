from trello import a

trello = TrelloApi("3d282ee48a4cb6018f7b4b1e15ca7cf9")
trello.boards.get('54819d8633dffb95de497060')


"""
{
    "closed": false,
    "desc": "Trello board used by the Trello team to track work on Trello.  How meta!\n\nThe development of the Trello API is being tracked at https://trello.com/api\n\nThe development of Trello Mobile applications is being tracked at https://trello.com/mobile",
    "id": "4d5ea62fd76aa1136000000c",
    "idOrganization": "4e1452614e4b8698470000e0",
    "name": "Trello Development",
    "pinned": true,
    "prefs": {
        "comments": "public",
        "invitations": "members",
        "permissionLevel": "public",
        "voting": "public"
    },
    "url": "https://trello.com/board/trello-development/4d5ea62fd76aa1136000000c"
}

"""