import { TestBed } from '@angular/core/testing';

import { StatDataService } from './stat-data.service';

describe('StatDataService', () => {
  let service: StatDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(StatDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
