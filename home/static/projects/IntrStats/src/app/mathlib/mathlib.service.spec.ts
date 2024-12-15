import { TestBed } from '@angular/core/testing';

import { MathlibService } from './mathlib.service';

describe('MathlibService', () => {
  let service: MathlibService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MathlibService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
