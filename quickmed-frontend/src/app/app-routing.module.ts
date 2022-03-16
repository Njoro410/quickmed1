import { IndexComponent } from './components/index/index.component';
import { RegisterComponent } from './components/register/register.component';
import { MedicineComponent } from './components/medicine/medicine.component';
import { CheckoutComponent } from './checkout/checkout.component';
import { SuccessComponent } from './components/success/success.component';
import { LoginComponent } from './components/login/login.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';


const routes: Routes = [
  {path: '', redirectTo:"/index", pathMatch:"full"},
  {path: 'index', component:IndexComponent},
  {path: 'register',component:RegisterComponent},
  {path: 'login',component:LoginComponent},
  {path: 'medicine',component:MedicineComponent},
  {path: 'checkout',component:CheckoutComponent},
  {path: 'success',component:SuccessComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
