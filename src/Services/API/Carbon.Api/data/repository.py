import json
from logging import Logger
from pprint import pprint
from typing import Any, Dict, Generic, List, NewType, Tuple, Type, TypeVar
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from fastapi.encoders import jsonable_encoder
from pymongo import ReturnDocument

from customLogging.logger import ILogger
from entities.baseEntity import BaseEntity

T = TypeVar("T", bound=BaseEntity)

class Repository(Generic[T]):

    _collection: AsyncIOMotorCollection
    _logger: Logger

    def __init__(self, collection: AsyncIOMotorCollection, logger: Logger = Depends(ILogger)) -> None:
        self._collection = collection
        self._logger = logger

    async def AddAsync(self, entity: T) -> Any | None:
        """
        Creates a new record of type T
        return the created entity in dict format if created or None

        :param entity: Entity object of type T
        """

        try:
            newEntity = jsonable_encoder(entity)
            _entity = await self._collection.insert_one(newEntity)
            createdEntity = await self._collection.find_one({"_id": _entity.inserted_id})
            return createdEntity
        except Exception as e:
            self._logger.error(f"Error while creating {type(entity)}: {e}")
            return None

    async def AddRangeAsync(self, entities: List[T]) -> Any | None:
        """
        Creates new records from the list of entity objects of type T
        return the list of created entities in dict format or None

        :param entities: list of entity objects of type T
        """

        try:
            newEntitites = jsonable_encoder(entities)
            _entities = await self._collection.insert_many(newEntitites)
            createdEntities = self._collection.find({"_id": {"$in":_entities.inserted_ids}})
            return await createdEntities.to_list(None)

        except Exception as e:
            self._logger.error(f"Error while creating {type(entities)}: {e}")
            return None

    async def UpdateAsync(self, entity: T, upsert: bool = False) -> Any | None:
        """
        Update entity of type T
        returns updated entity or None

        :param entity: entity to be updated of type T
        :param upsert (Optional): When True, inserts a new document if no document matches the query. Defaults to False.
        """
        dbEntity = await self._collection.find_one({"_id": entity.Id})

        if not dbEntity:
            self._logger.error(f"Entity of type {type(entity)} with Id = {entity.Id} not found!")
            return None

        try:
            _jsonEntity = jsonable_encoder(entity)
            updatedEntity = await self._collection.find_one_and_update({"_id": entity.Id}, {"$set": _jsonEntity}, return_document=ReturnDocument.AFTER, upsert=upsert)
            return updatedEntity

        except Exception as e:
            self._logger.error(f"Error while updating {type(entity)}: {e}")
            return None

    async def UpdateRangeAsync(self, entities: List[T]) -> Any | None:
        """
        Update the list of records
        returns updated records or None

        :param entities: List of Entities of type T
        """
        _updatedEntities = List[Any]

        try:
            for entity in entities:
                result = await self.UpdateAsync(entity, upsert=True)
                _updatedEntities.append(result)
            return _updatedEntities

        except Exception as e:
            self._logger.error(f"Error while updating {type(entities)}: {e}")
            return None

    async def UpdateRangeByPredicateAsync(self, update: dict, filterPredicate: dict={}) -> Any | None:
        return await self._collection.update_many(filter=filterPredicate, update={"$set": update})

    async def GetByIdAsync(self, id: str) -> Any | None:
        """
        Gets entity of type T having id
        returns record having _id equals to passed id

        :param id: Identifier of the record (_id field of the record)
        """
        return await self._collection.find_one({"_id": id})

    async def ListAsync(self, predicate: dict = {}, skip: int = 0, limit: int = 0, sort: List[Tuple[str, int]] = None) -> Any | None:
        """
        Gets the list of entity of type T based on parameters
        returns a list of records

        :param predicate:   (Optional)   filter dict
        :param skip:        (Optional)   skips first n records
        :param limit:       (Optional)   limits number of records
        :param sort:        (Optional)   sort keys with type
        """
        results = self._collection.find(filter=predicate, skip=skip, limit=limit, sort=sort)
        return await results.to_list(length=None)

    async def DeleteAsync(self, id: str) -> Any | None:
        """
        Marks any record of entity as Inactive
        returns deactivated record or None if not found

        :param id: Id of the record to be deactivated
        """
        dbEntity = await self._collection.find_one({"_id": id})

        if not dbEntity:
            self._logger.error(f"Entity of type {type(Type[T])} with Id = {id} not found!")
            return None

        try:
            deletedEntity = await self._collection.find_one_and_update({"_id": id}, {"$set": {"IsActive": False}}, return_document=ReturnDocument.AFTER)
            return deletedEntity

        except Exception as e:
            self._logger.error(f"Error while deleting {type(Type[T])}: {e}")
            return None

    async def IsExists(self, predicate: dict = {}) -> bool:
        """
        Checks if the record exists with the predicate

        :param predicate: filter conditions to find the record
        """
        dbEntity = await self._collection.find_one(filter=predicate)
        return True if dbEntity else False