import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CreditsService {
  path = environment.apiUrl + '/login'

  constructor(private httpClient: HttpClient) {
  }

  login(username: string, password: string): Observable<User> {
    const user: User = {
      username: username,
      password: password,
    }

    return this.httpClient.post<User>(this.path, user)
  }
}
