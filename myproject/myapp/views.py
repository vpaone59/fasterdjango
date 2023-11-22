# from django.shortcuts import render
from fastapi import APIRouter, HTTPException
from myapp.models import Animal
from myapp.schemas import AddAnimal, ReadAnimal

# Create your views here.

# creates an instance of APIRouter from FastAPI, which is used to define API routes
router = APIRouter()


@router.post("/animals", response_model=ReadAnimal)
def add_animal(animal: AddAnimal):
    animal_obj = Animal.objects.create(**animal.dict())
    return ReadAnimal(**animal_obj.__dict__)


@router.get("/animals/{animal_id}", response_model=ReadAnimal)
def read_animal(animal_id: int):
    try:
        animal = Animal.objects.get(pk=animal_id)
    except Animal.DoesNotExist:
        raise HTTPException(
            status_code=404, detail="Animal with such id does not exist."
        )
    return ReadAnimal(**animal.__dict__)
