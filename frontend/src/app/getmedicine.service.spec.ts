import { TestBed } from '@angular/core/testing';

import { GetmedicineService } from './getmedicine.service';

describe('GetmedicineService', () => {
  let service: GetmedicineService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetmedicineService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
