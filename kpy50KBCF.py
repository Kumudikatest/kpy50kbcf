import boto3
cognito_idp = boto3.client("cognito-idp")
from os import environ
ddb = boto3.client("dynamodb")

def handler(event, context):
    try:
        data = ddb.put_item(
            TableName="111",
            Item={
                'k': {
                    'S': "1"
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
        try:
            data = ddb.put_item(
                TableName="222",
                Item={
                    'k': {
                        'S': "1"
                    }
                }
            )
        except BaseException as e:
            print(e)
            raise(e)
            try:
                data = ddb.put_item(
                    TableName="333",
                    Item={
                        'k': {
                            'S': "1"
                        }
                    }
                )
            except BaseException as e:
                print(e)
                raise(e)
                try:
                    data = ddb.put_item(
                        TableName="444",
                        Item={
                            'k': {
                                'S': "1"
                            }
                        }
                    )
                except BaseException as e:
                    print(e)
                    raise(e)
    
                    try:
                        data = ddb.put_item(
                            TableName="555",
                            Item={
                                'k': {
                                    'S': "1"
                                }
                            }
                        )
                    except BaseException as e:
                        print(e)
                        raise(e)
                        try:
                            data = cognito_idp.list_users(
                                UserPoolId=environ["UserPoolId_cognito8"],
                                Limit=10
                            )
                        except BaseException as e:
                            print(e)
                            raise(e)
                            try:
                                data = cognito_idp.list_users(
                                    UserPoolId=environ["UserPoolId_cognito9"],
                                    Limit=10
                                )
                            except BaseException as e:
                                print(e)
                                raise(e)

                                try:
                                    data = cognito_idp.list_users(
                                        UserPoolId=environ["UserPoolId_cognito10"],
                                        Limit=10
                                    )
                                except BaseException as e:
                                    print(e)
                                    raise(e)
    
                                    try:
                                        data = cognito_idp.list_users(
                                            UserPoolId=environ["UserPoolId_cognito11"],
                                            Limit=10
                                        )
                                    except BaseException as e:
                                        print(e)
                                        raise(e)

                                        try:
                                            data = cognito_idp.list_users(
                                                UserPoolId=environ["UserPoolId_cognito12"],
                                                Limit=10
                                            )
                                        except BaseException as e:
                                            print(e)
                                            raise(e)
                   
                                            try:
                                                data = cognito_idp.list_users(
                                                    UserPoolId=environ["UserPoolId_cognito13"],
                                                    Limit=10
                                                )
                                            except BaseException as e:
                                                print(e)
                                                raise(e)
                                        
                                                try:
                                                    data = cognito_idp.list_users(
                                                        UserPoolId=environ["UserPoolId_cognito14"],
                                                        Limit=10
                                                    )
                                                except BaseException as e:
                                                    print(e)
                                                    raise(e)
                                                    try:
                                                        data = cognito_idp.list_users(
                                                            UserPoolId=environ["UserPoolId_cognito15"],
                                                            Limit=10
                                                        )
                                                    except BaseException as e:
                                                        print(e)
                                                        raise(e)
    
                                                        try:
                                                            data = cognito_idp.list_users(
                                                                UserPoolId=environ["UserPoolId_cognito16"],
                                                                Limit=10
                                                            )
                                                        except BaseException as e:
                                                            print(e)
                                                            raise(e)
                                                            try:
                                                                data = cognito_idp.list_users(
                                                                    UserPoolId=environ["UserPoolId_cognito17"],
                                                                    Limit=10
                                                                )
                                                            except BaseException as e:
                                                                print(e)
                                                                raise(e)

                                                                try:
                                                                    data = cognito_idp.list_users(
                                                                        UserPoolId=environ["UserPoolId_cognito18"],
                                                                        Limit=10
                                                                    )
                                                                except BaseException as e:
                                                                    print(e)
                                                                    raise(e)
          
                                                                    try:
                                                                        data = cognito_idp.list_users(
                                                                            UserPoolId=environ["UserPoolId_cognito19"],
                                                                            Limit=10
                                                                        )
                                                                    except BaseException as e:
                                                                        print(e)
                                                                        raise(e)
                                                                        try:
                                                                            data = cognito_idp.list_users(
                                                                                UserPoolId=environ["UserPoolId_cognito20"],
                                                                                Limit=10
                                                                            )
                                                                        except BaseException as e:
                                                                            print(e)
                                                                            raise(e)
                                                            
    
    return {"message": "Successfully executed"}
