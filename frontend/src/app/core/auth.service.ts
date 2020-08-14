import { Injectable } from '@angular/core'
import {HttpClient, HttpErrorResponse, HttpParams} from '@angular/common/http'
import { Observable } from 'rxjs'
import { environment } from 'src/environments/environment'
import { User } from '../modules/users/models/user.model'
import { stringify } from 'querystring'

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  path = environment.apiUrl + '/login'

  constructor(private httpClient: HttpClient) {
  }

  login(username: string, password: string): Observable<User> {
    const params = new HttpParams()
      .set('username', username)
      .set('password', password)
    return this.httpClient.post<User>(this.path, {params})
  }

}
