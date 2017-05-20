// CalculDlg.h : header file
//

#if !defined(AFX_CALCULDLG_H__CE774AA2_3E59_42B7_8D69_684558FE2B92__INCLUDED_)
#define AFX_CALCULDLG_H__CE774AA2_3E59_42B7_8D69_684558FE2B92__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CCalculDlg dialog

class CCalculDlg : public CDialog
{
// Construction
public:
	CCalculDlg(CWnd* pParent = NULL);	// standard constructor
	void GetNum(CString num);
// Dialog Data
	//{{AFX_DATA(CCalculDlg)
	enum { IDD = IDD_CALCUL_DIALOG };
	CString	m_N0;
	double	m_N1;
	double	m_N2;
	double  m_M;
	int e;
	CString	m_Result;
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CCalculDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	//{{AFX_MSG(CCalculDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnButton1();
	afx_msg void OnButton2();
	afx_msg void OnButton3();
	afx_msg void OnButton4();
	afx_msg void OnButton5();
	afx_msg void OnButton6();
	afx_msg void OnButton7();
	afx_msg void OnButton8();
	afx_msg void OnButton9();
	afx_msg void OnButton10();
	afx_msg void OnButton11();
	afx_msg void OnButton12();
	afx_msg void OnButton13();
	afx_msg void OnButton14();
	afx_msg void OnButton15();
	afx_msg void OnButton16();
	afx_msg void OnButton17();
	afx_msg void OnButton18();
	afx_msg void OnButton19();
	afx_msg void OnButton20();
	afx_msg void OnButton21();
	afx_msg void OnButton27();
	afx_msg void OnButton26();
	afx_msg void OnButton25();
	afx_msg void OnButton24();
	afx_msg void OnButton23();
	afx_msg void OnButton22();
	afx_msg void OnAppAbout();
	afx_msg void OnEditCopy();
	afx_msg void OnEditPaste();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_CALCULDLG_H__CE774AA2_3E59_42B7_8D69_684558FE2B92__INCLUDED_)
