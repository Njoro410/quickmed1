import { Component, OnInit } from '@angular/core';
import { Medicine } from 'src/app/medicine';
import { GetmedicineService } from 'src/app/getmedicine.service';

@Component({
  selector: 'app-prescription',
  templateUrl: './prescription.component.html',
  styleUrls: ['./prescription.component.css']
})
export class PrescriptionComponent implements OnInit {
  dawa: Medicine[] = [];

  constructor( private medicine: GetmedicineService ) { }



  ngOnInit(): void {
    this.medicine.getPrescriptionMedicine().subscribe(data => {
      this.dawa = data
    })
    console.log(this.dawa)
  }

}
