import { Entity } from 'src/app/shared/models/entity.model';

export interface Person extends Entity {
    name: string
    last_name: string
    email: string
    document: string
}