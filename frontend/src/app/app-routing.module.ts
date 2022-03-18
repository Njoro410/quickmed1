import { OTCComponent } from './components/otc/otc.component';
import { IndexComponent } from './components/index/index.component';
import { RegisterComponent } from './components/register/register.component';
import { MedicineComponent } from './components/medicine/medicine.component';
import { SuccessComponent } from './components/success/success.component';
import { LoginComponent } from './components/login/login.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrescriptionComponent } from './components/prescription/prescription.component';
import { CheckoutComponent } from './components/checkout/checkout.component';



const routes: Routes = [
  {path: '', redirectTo:"/index", pathMatch:"full"},
  {path: 'index', component:IndexComponent},
  {path: 'register',component:RegisterComponent},
  {path: 'login',component:LoginComponent},
  {path: 'medicine',component:MedicineComponent},
  {path: 'success',component:SuccessComponent},
  {path: 'prescription', component:PrescriptionComponent},
  {path: 'otc', component:OTCComponent},
  {path: 'checkout', component:CheckoutComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
