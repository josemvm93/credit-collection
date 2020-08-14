import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './modules/login/login.component';
import { UsersModule } from './modules/users/users.module';
import { IndicatorsModule } from './modules/indicators/indicators.module';
import { CreditsModule } from './modules/credits/credits.module';
import { LoginModule } from './modules/login/login.module';
import { PrincipalModule } from './modules/principal/principal.module';
import { CoreModule } from './core/core.module';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    LoginModule,
    UsersModule,
    IndicatorsModule,
    CreditsModule,
    PrincipalModule,
    CoreModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
