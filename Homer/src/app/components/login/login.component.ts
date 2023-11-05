import { Component } from "@angular/core";
import { OnInit } from "@angular/core";
import { Router } from '@angular/router';

@Component({
  selector: "cl-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.css"]
})
export class LoginComponent implements OnInit {
  constructor(private router: Router) {}

  ngOnInit(): void {}

  navigateToRegisterPage() {
    this.router.navigate(['/components/register/register.component']); // Replace 'register' with the actual route path of your register page
  }
}
