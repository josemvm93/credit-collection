import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from 'src/app/core/auth.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit, OnDestroy {
  form: FormGroup
  loginInvalid: boolean = false
  subscription: Subscription

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private authService: AuthService
  ) { }

  ngOnInit(): void {
    this.builForm()
  }

  ngOnDestroy() {
    this.subscription && this.subscription.unsubscribe()
  }

  builForm() {
    this.form = this.fb.group({
      username: ['', Validators.email],
      password: ['', Validators.required]
    })
  }

  onLogin() {
    if ( this.form.valid) {
      this.subscription = this.authService.login(this.form.get('username').value, this.form.get('password').value).subscribe(
        user => {
          localStorage.setItem('user', JSON.stringify(user))
          this.loginInvalid = false
          this.router.navigate(['../principal'], {relativeTo: this.route})
        },
        error => {
          this.loginInvalid = true
        }
      )
    }
  }

}
