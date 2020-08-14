import { Component, OnInit } from '@angular/core';
import { SidenavService } from '../side-nav/side-nav.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  hidden = false;

  toggleBadgeVisibility() {
    this.hidden = !this.hidden;
  }

  constructor(private sideNavService: SidenavService) { }

  ngOnInit(): void {
  }

  openMenu() {
    console.log('menu')
    this.sideNavService.toggle()
  }

}
