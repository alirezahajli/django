import graphene
import data.schema


class Query(data.schema.CurrenciesDataQuery, graphene.ObjectType):
    pass


# class Mutation(home.schema.Mutate, accounts.schema.Mutation, graphene.ObjectType):
# 	pass


schema = graphene.Schema(query=Query)
