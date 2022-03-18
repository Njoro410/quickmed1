import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Medicine } from './medicine';
import { Observable } from 'rxjs';
import { ThisReceiver } from '@angular/compiler';


@Injectable({
  providedIn: 'root'
})
export class GetmedicineService {
  medicine!: Medicine[]
  apiRoot: string = 'http://127.0.0.1:5000/medicine'
  apiRoot1: string = 'http://127.0.0.1:5000/medicine/prescription'
  apiRoot2: string = 'http://127.0.0.1:5000/medicine/otc'

  constructor(private http: HttpClient) {
    this.medicine = []
  }



  getMedicine(): Observable<Medicine[]> {
    let apiUrl = this.apiRoot
    return this.http.get<Medicine[]>
      (apiUrl)
  }
  getPrescriptionMedicine(): Observable<Medicine[]> {
    let apiUrl = this.apiRoot1
    return this.http.get<Medicine[]>
      (apiUrl)
  }
  getOTCMedicine(): Observable<Medicine[]> {
    let apiUrl = this.apiRoot2
    return this.http.get<Medicine[]>
      (apiUrl)
  }
}
