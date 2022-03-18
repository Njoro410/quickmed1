import { Component, OnInit } from '@angular/core';
import { Medicine } from 'src/app/medicine';
import { GetmedicineService } from 'src/app/getmedicine.service';

@Component({
  selector: 'app-otc',
  templateUrl: './otc.component.html',
  styleUrls: ['./otc.component.css']
})
export class OTCComponent implements OnInit {

  dawa: Medicine[] = [];

  constructor( private medicine: GetmedicineService ) { }



  ngOnInit(): void {
    this.medicine.getOTCMedicine().subscribe(data => {
      this.dawa = data
    })
    console.log(this.dawa)
  }
}
