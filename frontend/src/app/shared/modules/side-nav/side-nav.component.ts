import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { SidenavService } from './side-nav.service';
import { MatSidenav } from '@angular/material/sidenav';

@Component({
  selector: 'app-side-nav',
  templateUrl: './side-nav.component.html',
  styleUrls: ['./side-nav.component.scss']
})
export class SideNavComponent implements OnInit, AfterViewInit {  
  @ViewChild('sidenav') public sidenav: MatSidenav;
  
  constructor(private sideNavService: SidenavService) { }

  ngOnInit(): void {
  }

  ngAfterViewInit() {
    this.sideNavService.setSidenav(this.sidenav)
  }

}
