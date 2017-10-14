from trello import TrelloClient
trelloToken = '01d4de8a2bb9834bad8e391db57fea9b725eb1cd9bd1eb70a9322bd411d3dd2c'
trelloKey = 'd819cf1999de0187fae50f89aed19ae1'
trelloSecret = '534fcf3f550bbfe33961bbf2c700a4448ed5273326993b776a067e477f3f6fb6'

client = TrelloClient(
    api_key = trelloKey,
    api_secret=trelloSecret,
    token=trelloToken,
    token_secret=None
)

all_boards = client.list_boards()
for board in all_boards:
    print board.name
