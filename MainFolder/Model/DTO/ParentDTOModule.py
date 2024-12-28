from abc import ABC, abstractmethod

from MainFolder.Model.DTO.DTO import DTO


class ParentDTOModule(ABC):
    @abstractmethod
    def return_dto(self) -> DTO:
        pass
