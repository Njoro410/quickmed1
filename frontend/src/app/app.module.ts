import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IndexComponent } from './components/index/index.component';
import { RegisterComponent } from './components/register/register.component';
import { MedicineComponent } from './components/medicine/medicine.component';
import { SuccessComponent } from './components/success/success.component';
import { LoginComponent } from './components/login/login.component';
import { CheckoutComponent } from './components/checkout/checkout.component';
import { GetmedicineService } from './getmedicine.service';
import { HttpClientModule } from '@angular/common/http';
import { PrescriptionComponent } from './components/prescription/prescription.component';
import { OTCComponent } from './components/otc/otc.component';

@NgModule({
  declarations: [
    AppComponent,
    MedicineComponent,
    SuccessComponent,
    LoginComponent,
    RegisterComponent,
    IndexComponent,
    CheckoutComponent,
    PrescriptionComponent,
    OTCComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [GetmedicineService],
  bootstrap: [AppComponent]
})
export class AppModule { }
