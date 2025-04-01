from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    @abstractmethod
    def update(self, cam):
        pass

    @abstractmethod
    def draw(self, screen, camera):
        pass

class CompositeEntity(Entity):
    def __init__(self):
        self.entities = []
        self.rect = pygame.Rect(0, 0, 0, 0)  # Default rect; will be updated

    def add(self, entity):
        self.entities.append(entity)
        self.update_rect()  # Update bounding box when adding an entity

    def update_rect(self):
        """ Update self.rect to encompass all child entities """
        if not self.entities:
            self.rect = pygame.Rect(0, 0, 0, 0)  # Reset if no entities
            return

        x_min = min(entity.rect.left for entity in self.entities if hasattr(entity, "rect"))
        y_min = min(entity.rect.top for entity in self.entities if hasattr(entity, "rect"))
        x_max = max(entity.rect.right for entity in self.entities if hasattr(entity, "rect"))
        y_max = max(entity.rect.bottom for entity in self.entities if hasattr(entity, "rect"))

        self.rect = pygame.Rect(x_min, y_min, x_max - x_min, y_max - y_min)

    def remove(self, entity):
        self.entities.remove(entity)
        self.update_rect()  # Update bounding box when removing an entity

    def __iter__(self):
        return iter(self.entities)  # Allow iteration

    def update(self, cam):
        for entity in self.entities:
            entity.update(cam)
            if hasattr(entity, "alive") and not entity.alive:
                self.remove(entity)
        self.update_rect()  # Update bounding box after movement

    def draw(self, screen, camera):
        for entity in self.entities:
            entity.draw(screen, camera)
