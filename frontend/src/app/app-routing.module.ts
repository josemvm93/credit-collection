import { Routes, RouterModule } from "@angular/router";
import { LoginComponent } from './modules/login/login.component';
import { NgModule } from '@angular/core';
import { PrincipalComponent } from './modules/principal/principal.component';

const routes: Routes = [
    { path: '', pathMatch: 'full', redirectTo: '/login' },
    { path: 'login', component: LoginComponent },
    { path: 'principal', component: PrincipalComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule { }