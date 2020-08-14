import { Injectable } from '@angular/core'
import {HttpClient, HttpErrorResponse} from '@angular/common/http'
import { Observable } from 'rxjs'
import { User } from './models/user.model'
import { environment } from 'src/environments/environment'

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  path = environment.apiUrl + '/users'

  constructor(private httpClient: HttpClient) {
  }

  // private static _handleError(err: HttpErrorResponse | any ) {
  //   return Observable.throw(err.message || 'Error: Unable to complete request.')
  // }

  getUser(): Observable<User[]> {
    return this.httpClient
      .get<User[]>(this.path)
      // .catch(UsersService._handleError)
  }

}
