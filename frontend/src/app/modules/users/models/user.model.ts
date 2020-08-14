import { Entity } from 'src/app/shared/models/entity.model';

export interface User extends Entity {
    username: string
    password: string
    person_id: number
    rol: number
}