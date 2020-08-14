import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { SideNavComponent } from './side-nav.component'

import { MatSidenavModule } from '@angular/material/sidenav'
import { MatMenuModule } from '@angular/material/menu'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatListModule } from '@angular/material/list'
import { SidenavService } from './side-nav.service'



@NgModule({
  declarations: [SideNavComponent],
  imports: [
    CommonModule,
    MatSidenavModule,
    MatMenuModule,
    MatButtonModule,
    MatIconModule,
    MatListModule
  ],
  exports: [SideNavComponent],
  providers: [SidenavService]
})
export class SideNavModule { }
