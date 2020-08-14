import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { PrincipalComponent } from './principal.component'
import { HeaderModule } from 'src/app/shared/modules/header/header.module'
import { SideNavModule } from 'src/app/shared/modules/side-nav/side-nav.module'
import { PrincipalRoutingModule } from './principal.routing.module'

@NgModule({
  declarations: [PrincipalComponent],
  imports: [
    CommonModule,
    HeaderModule,
    SideNavModule,
    PrincipalRoutingModule
  ]
})
export class PrincipalModule { }
