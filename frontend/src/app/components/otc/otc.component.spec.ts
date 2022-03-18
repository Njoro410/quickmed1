import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OTCComponent } from './otc.component';

describe('OTCComponent', () => {
  let component: OTCComponent;
  let fixture: ComponentFixture<OTCComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OTCComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OTCComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
