import { Component, OnInit } from '@angular/core';
import { Medicine } from 'src/app/medicine';
import { GetmedicineService } from 'src/app/getmedicine.service';

@Component({
  selector: 'app-medicine',
  templateUrl: './medicine.component.html',
  styleUrls: ['./medicine.component.css']
})
export class MedicineComponent implements OnInit {

  dawa: Medicine[] = [];

  constructor( private medicine: GetmedicineService ) { }



  ngOnInit(): void {
    this.medicine.getMedicine().subscribe(data => {
      this.dawa = data
    })
    console.log(this.dawa)
  }

}
