import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';


import {MatButtonModule} from '@angular/material/button'
import {MatIconModule} from '@angular/material/icon'
import {MatToolbarModule} from '@angular/material/toolbar'
import {MatBadgeModule} from '@angular/material/badge'

import { HeaderComponent } from './header.component'


@NgModule({
  declarations: [HeaderComponent],
  imports: [
    CommonModule,
    MatButtonModule,
    MatIconModule,
    MatToolbarModule,
    MatBadgeModule
  ],
  exports: [
    HeaderComponent
  ]
})
export class HeaderModule { }
