import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router'; // Import the RouterModule
import { AppComponent } from './app.component';
import { ClLoginComponent } from './path-to-cl-login/cl-login.component';



@NgModule({
  declarations: [
    AppComponent,
    ClLoginComponent, // Add ClLoginComponent to the declarations array
  ],
  imports: [
    BrowserModule,
    RouterModule, // Add RouterModule to the imports array
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
