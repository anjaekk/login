import pytest
from aiographql.client import GraphQLRequest


async def test_create_user(graphql_client):
    query = """
        mutation createUser{
        createUser(inputData: { 
        email: "test@test.com", 
        password: "123456",
        name: "test"
        }) {
            user{
            name
            email
        }
        }
    }
    """
    result = graphql_client.execute(query)
    print(result)
    print("*************")
    assert result['data']['createUser']['name'] == "test"
    assert 'errors' not in result